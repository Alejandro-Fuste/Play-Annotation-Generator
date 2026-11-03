# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_21`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
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
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [75-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-107] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-102] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-155] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-154] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-209] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.