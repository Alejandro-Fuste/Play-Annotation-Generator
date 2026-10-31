# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_38`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '7' has invalid range: start=139, end=45. Clamping end to start.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [2–6], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=7.
> - Segment 'Action_ThrowPass' for track '18' has invalid range: start=83, end=36. Clamping end to start.
> - Action 'Action_None' range [2-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-41] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-111] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-204] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-188] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_RunHitchRoute' range [14-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-182] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-23] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-41] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-77] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-12] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-6] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-12] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-8] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-8] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-44] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-54] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-7] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 7, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [7-7] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '19' starts at frame 5, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [5-7] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-21] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-42] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-82] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-113] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-201] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-160] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-176] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '40' has 2 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.