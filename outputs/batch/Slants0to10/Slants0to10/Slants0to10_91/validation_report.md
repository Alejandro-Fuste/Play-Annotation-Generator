# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_91`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 68 |
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
> - Segment 'Action_BallCarry' for track '4' has invalid range: start=80, end=72. Clamping end to start.
> - Action 'Action_PreSnap' range [0-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunSlantRoute' range [5-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-84] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-80] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-60] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-103] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-121] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-29] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-132] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-159] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-105] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-117] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-130] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-211] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-157] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-154] for track '31' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.