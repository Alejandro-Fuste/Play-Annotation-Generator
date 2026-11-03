# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_133`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_133/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-61] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-129] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-148] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-141] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-78] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-90] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-81] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-133] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-170] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '32' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.