# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_32`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 122 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–11], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=12.
> - Action 'Action_None' range [1-72] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-197] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-22] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-22] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-145] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-50] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-22] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-98] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-145] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-22] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-38] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-49] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-68] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-95] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-142] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-152] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [154-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-120] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_RunHitchRoute' range [20-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [114-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [173-187] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-172] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-73] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [90-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-188] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-95] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-102] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [121-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [124-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [167-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [174-209] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-58] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-95] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [138-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [174-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-139] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-208] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-207] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-196] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '32' has 1 frames without a visible bounding box.
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