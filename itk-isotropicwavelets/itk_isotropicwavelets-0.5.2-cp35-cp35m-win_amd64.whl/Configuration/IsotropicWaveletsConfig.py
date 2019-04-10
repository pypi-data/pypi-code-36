depends = ('ITKPyBase', 'ITKRegistrationCommon', 'ITKImageFunction', 'ITKImageFrequency', 'ITKFFT', 'ITKConvolution', )
templates = (
  ('Image', 'itk::Image', 'itkImageVSM2', False, 'itk::VariableSizeMatrix< double >, 2'),
  ('Image', 'itk::Image', 'itkImageVSM3', False, 'itk::VariableSizeMatrix< double >, 3'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceVSM2', False, 'itk::Image<itk::VariableSizeMatrix< double >, 2 >'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceVSM3', False, 'itk::Image<itk::VariableSizeMatrix< double >, 3 >'),
  ('ImageToImageFilter', 'itk::ImageToImageFilter', 'itkImageToImageFilterIF2VSM2', False, 'itk::Image< float,2 >, itk::Image<itk::VariableSizeMatrix< double >, 2 >'),
  ('ImageToImageFilter', 'itk::ImageToImageFilter', 'itkImageToImageFilterIF3VSM3', False, 'itk::Image< float,3 >, itk::Image<itk::VariableSizeMatrix< double >, 3 >'),
  ('StructureTensor', 'itk::StructureTensor', 'itkStructureTensorIF2VSM2', True, 'itk::Image< float,2 >, itk::Image<itk::VariableSizeMatrix< double >, 2 >'),
  ('StructureTensor', 'itk::StructureTensor', 'itkStructureTensorIF3VSM3', True, 'itk::Image< float,3 >, itk::Image<itk::VariableSizeMatrix< double >, 3 >'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceVICF2', False, 'itk::VectorImage< std::complex< float >,2 >'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceVICF3', False, 'itk::VectorImage< std::complex< float >,3 >'),
  ('ImageToImageFilter', 'itk::ImageToImageFilter', 'itkImageToImageFilterICF2VICF2', False, 'itk::Image< std::complex< float >,2 >, itk::VectorImage< std::complex< float >,2 >'),
  ('ImageToImageFilter', 'itk::ImageToImageFilter', 'itkImageToImageFilterICF3VICF3', False, 'itk::Image< std::complex< float >,3 >, itk::VectorImage< std::complex< float >,3 >'),
  ('MonogenicSignalFrequencyImageFilter', 'itk::MonogenicSignalFrequencyImageFilter', 'itkMonogenicSignalFrequencyImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('MonogenicSignalFrequencyImageFilter', 'itk::MonogenicSignalFrequencyImageFilter', 'itkMonogenicSignalFrequencyImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('ImageToImageFilter', 'itk::ImageToImageFilter', 'itkImageToImageFilterVICF2VIF2', False, 'itk::VectorImage< std::complex< float >,2 >, itk::VectorImage< float,2 >'),
  ('ImageToImageFilter', 'itk::ImageToImageFilter', 'itkImageToImageFilterVICF3VIF3', False, 'itk::VectorImage< std::complex< float >,3 >, itk::VectorImage< float,3 >'),
  ('VectorInverseFFTImageFilter', 'itk::VectorInverseFFTImageFilter', 'itkVectorInverseFFTImageFilterVICF2VIF2', True, 'itk::VectorImage< std::complex< float >,2 >, itk::VectorImage< float,2 >'),
  ('VectorInverseFFTImageFilter', 'itk::VectorInverseFFTImageFilter', 'itkVectorInverseFFTImageFilterVICF3VIF3', True, 'itk::VectorImage< std::complex< float >,3 >, itk::VectorImage< float,3 >'),
  ('FrequencyExpandImageFilter', 'itk::FrequencyExpandImageFilter', 'itkFrequencyExpandImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('FrequencyExpandImageFilter', 'itk::FrequencyExpandImageFilter', 'itkFrequencyExpandImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('FrequencyExpandViaInverseFFTImageFilter', 'itk::FrequencyExpandViaInverseFFTImageFilter', 'itkFrequencyExpandViaInverseFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('FrequencyExpandViaInverseFFTImageFilter', 'itk::FrequencyExpandViaInverseFFTImageFilter', 'itkFrequencyExpandViaInverseFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('FrequencyFunction', 'itk::FrequencyFunction', 'itkFrequencyFunctionF2PD2', True, 'float, 2, itk::Point< double,2 >'),
  ('FrequencyFunction', 'itk::FrequencyFunction', 'itkFrequencyFunctionF3PD3', True, 'float, 3, itk::Point< double,3 >'),
  ('FrequencyShrinkImageFilter', 'itk::FrequencyShrinkImageFilter', 'itkFrequencyShrinkImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('FrequencyShrinkImageFilter', 'itk::FrequencyShrinkImageFilter', 'itkFrequencyShrinkImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('FrequencyShrinkViaInverseFFTImageFilter', 'itk::FrequencyShrinkViaInverseFFTImageFilter', 'itkFrequencyShrinkViaInverseFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('FrequencyShrinkViaInverseFFTImageFilter', 'itk::FrequencyShrinkViaInverseFFTImageFilter', 'itkFrequencyShrinkViaInverseFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('HeldIsotropicWavelet', 'itk::HeldIsotropicWavelet', 'itkHeldIsotropicWaveletF2PD2', True, 'float, 2, itk::Point< double,2 >'),
  ('HeldIsotropicWavelet', 'itk::HeldIsotropicWavelet', 'itkHeldIsotropicWaveletF3PD3', True, 'float, 3, itk::Point< double,3 >'),
  ('IsotropicFrequencyFunction', 'itk::IsotropicFrequencyFunction', 'itkIsotropicFrequencyFunctionF2PD2', True, 'float, 2, itk::Point< double,2 >'),
  ('IsotropicFrequencyFunction', 'itk::IsotropicFrequencyFunction', 'itkIsotropicFrequencyFunctionF3PD3', True, 'float, 3, itk::Point< double,3 >'),
  ('IsotropicWaveletFrequencyFunction', 'itk::IsotropicWaveletFrequencyFunction', 'itkIsotropicWaveletFrequencyFunctionF2PD2', True, 'float, 2, itk::Point< double,2 >'),
  ('IsotropicWaveletFrequencyFunction', 'itk::IsotropicWaveletFrequencyFunction', 'itkIsotropicWaveletFrequencyFunctionF3PD3', True, 'float, 3, itk::Point< double,3 >'),
  ('PhaseAnalysisImageFilter', 'itk::PhaseAnalysisImageFilter', 'itkPhaseAnalysisImageFilterVIF2IF2', True, 'itk::VectorImage< float,2 >, itk::Image< float,2 >'),
  ('PhaseAnalysisImageFilter', 'itk::PhaseAnalysisImageFilter', 'itkPhaseAnalysisImageFilterVIF3IF3', True, 'itk::VectorImage< float,3 >, itk::Image< float,3 >'),
  ('PhaseAnalysisSoftThresholdImageFilter', 'itk::PhaseAnalysisSoftThresholdImageFilter', 'itkPhaseAnalysisSoftThresholdImageFilterVIF2IF2', True, 'itk::VectorImage< float,2 >, itk::Image< float,2 >'),
  ('PhaseAnalysisSoftThresholdImageFilter', 'itk::PhaseAnalysisSoftThresholdImageFilter', 'itkPhaseAnalysisSoftThresholdImageFilterVIF3IF3', True, 'itk::VectorImage< float,3 >, itk::Image< float,3 >'),
  ('RieszFrequencyFilterBankGenerator', 'itk::RieszFrequencyFilterBankGenerator', 'itkRieszFrequencyFilterBankGeneratorICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('RieszFrequencyFilterBankGenerator', 'itk::RieszFrequencyFilterBankGenerator', 'itkRieszFrequencyFilterBankGeneratorICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('RieszRotationMatrix', 'itk::RieszRotationMatrix', 'itkRieszRotationMatrixD2', True, 'double,2'),
  ('RieszRotationMatrix', 'itk::RieszRotationMatrix', 'itkRieszRotationMatrixD3', True, 'double,3'),
  ('ShannonIsotropicWavelet', 'itk::ShannonIsotropicWavelet', 'itkShannonIsotropicWaveletF2PD2', True, 'float, 2, itk::Point< double,2 >'),
  ('ShannonIsotropicWavelet', 'itk::ShannonIsotropicWavelet', 'itkShannonIsotropicWaveletF3PD3', True, 'float, 3, itk::Point< double,3 >'),
  ('SimoncelliIsotropicWavelet', 'itk::SimoncelliIsotropicWavelet', 'itkSimoncelliIsotropicWaveletF2PD2', True, 'float, 2, itk::Point< double,2 >'),
  ('SimoncelliIsotropicWavelet', 'itk::SimoncelliIsotropicWavelet', 'itkSimoncelliIsotropicWaveletF3PD3', True, 'float, 3, itk::Point< double,3 >'),
  ('VowIsotropicWavelet', 'itk::VowIsotropicWavelet', 'itkVowIsotropicWaveletF2PD2', True, 'float, 2, itk::Point< double,2 >'),
  ('VowIsotropicWavelet', 'itk::VowIsotropicWavelet', 'itkVowIsotropicWaveletF3PD3', True, 'float, 3, itk::Point< double,3 >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF2VowF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::VowIsotropicWavelet< float, 2, itk::Point< double,2 > >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF2HeldF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::HeldIsotropicWavelet< float, 2, itk::Point< double,2 > >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF2SimoncelliF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::SimoncelliIsotropicWavelet< float, 2, itk::Point< double,2 > >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF2ShannonF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::ShannonIsotropicWavelet< float, 2, itk::Point< double,2 > >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF3VowF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::VowIsotropicWavelet< float, 3, itk::Point< double,3 > >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF3HeldF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::HeldIsotropicWavelet< float, 3, itk::Point< double,3 > >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF3SimoncelliF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::SimoncelliIsotropicWavelet< float, 3, itk::Point< double,3 > >'),
  ('WaveletFrequencyFilterBankGenerator', 'itk::WaveletFrequencyFilterBankGenerator', 'itkWaveletFrequencyFilterBankGeneratorICF3ShannonF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::ShannonIsotropicWavelet< float, 3, itk::Point< double,3 > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF2ICF2VowF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::VowIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF2ICF2HeldF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::HeldIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF2ICF2SimoncelliF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::SimoncelliIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF2ICF2ShannonF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::ShannonIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF3ICF3VowF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::VowIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF3ICF3HeldF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::HeldIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF3ICF3SimoncelliF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::SimoncelliIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyForward', 'itk::WaveletFrequencyForward', 'itkWaveletFrequencyForwardICF3ICF3ShannonF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::ShannonIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF2ICF2VowF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::VowIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF2ICF2HeldF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::HeldIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF2ICF2SimoncelliF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::SimoncelliIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF2ICF2ShannonF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::ShannonIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF3ICF3VowF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::VowIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF3ICF3HeldF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::HeldIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF3ICF3SimoncelliF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::SimoncelliIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyForwardUndecimated', 'itk::WaveletFrequencyForwardUndecimated', 'itkWaveletFrequencyForwardUndecimatedICF3ICF3ShannonF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::ShannonIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF2ICF2VowF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::VowIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF2ICF2HeldF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::HeldIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF2ICF2SimoncelliF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::SimoncelliIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF2ICF2ShannonF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::ShannonIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF3ICF3VowF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::VowIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF3ICF3HeldF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::HeldIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF3ICF3SimoncelliF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::SimoncelliIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverse', 'itk::WaveletFrequencyInverse', 'itkWaveletFrequencyInverseICF3ICF3ShannonF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::ShannonIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF2ICF2VowF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::VowIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF2ICF2HeldF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::HeldIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF2ICF2SimoncelliF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::SimoncelliIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF2ICF2ShannonF2PD2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,2 >, itk::ShannonIsotropicWavelet< float, 2, itk::Point< double,2 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF3ICF3VowF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::VowIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF3ICF3HeldF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::HeldIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF3ICF3SimoncelliF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::SimoncelliIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('WaveletFrequencyInverseUndecimated', 'itk::WaveletFrequencyInverseUndecimated', 'itkWaveletFrequencyInverseUndecimatedICF3ICF3ShannonF3PD3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >, itk::WaveletFrequencyFilterBankGenerator< itk::Image< std::complex< float >,3 >, itk::ShannonIsotropicWavelet< float, 3, itk::Point< double,3 > > >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterISS2', True, 'itk::Image< signed short,2 >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterISS3', True, 'itk::Image< signed short,3 >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('ZeroDCImageFilter', 'itk::ZeroDCImageFilter', 'itkZeroDCImageFilterIF3', True, 'itk::Image< float,3 >'),
)
snake_case_functions = ('wavelet_frequency_inverse_undecimated', 'image_source', 'riesz_frequency_filter_bank_generator', 'monogenic_signal_frequency_image_filter', 'wavelet_frequency_forward', 'vector_inverse_fft_image_filter', 'frequency_expand_image_filter', 'frequency_shrink_via_inverse_fft_image_filter', 'frequency_shrink_image_filter', 'wavelet_frequency_filter_bank_generator', 'image_to_image_filter', 'wavelet_frequency_inverse', 'frequency_expand_via_inverse_fft_image_filter', 'zero_dc_image_filter', 'phase_analysis_image_filter', 'phase_analysis_soft_threshold_image_filter', 'wavelet_frequency_forward_undecimated', 'structure_tensor', )
