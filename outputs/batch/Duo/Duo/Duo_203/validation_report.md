# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_203`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-145] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-196] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-156] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-181] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-200] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-200] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-137] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-174] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-199] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-184] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [117-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-154] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [117-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-174] for track '24' has 2 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.