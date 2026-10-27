# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_93`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 374 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 374 as fallback play end.
> - Action 'Action_None' range [274-300] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-374] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-337] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-331] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [304-356] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-304] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-355] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-363] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-306] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-357] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-328] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-374] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-86] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-108] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-339] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-356] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-371] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-358] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-348] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.