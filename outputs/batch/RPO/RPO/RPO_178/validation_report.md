# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_178`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_178/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [27-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-63] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-177] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-67] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-37] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-139] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-16] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-180] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '30' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.