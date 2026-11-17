# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_90`
- **Input XML**: `outputs/batch/Power/Power/Power_90/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 182: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - Row 182: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 182: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PullBlock' range [51-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-190] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-206] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-182] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-55] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-82] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [51-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-200] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-167] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-166] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [51-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-139] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-155] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-147] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-157] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-210] for track '31' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.