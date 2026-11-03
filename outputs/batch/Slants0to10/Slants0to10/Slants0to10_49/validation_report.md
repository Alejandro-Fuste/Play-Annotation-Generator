# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_49`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [4–19], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=20.
> - Action 'Action_None' range [4-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-74] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-192] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-145] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-189] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-68] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-173] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-64] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-202] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-210] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-86] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-85] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-23] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-149] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-56] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-68] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '21' starts at frame 7, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [7-10] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-44] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-205] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '28' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.