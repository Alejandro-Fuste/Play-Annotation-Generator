# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_142`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_142/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ComboBlock' range [109-175] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [109-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [109-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-100] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-156] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-190] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-205] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-209] for track '22' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.