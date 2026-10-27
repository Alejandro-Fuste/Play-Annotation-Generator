# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_210`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_210/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [59-100] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-266] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [138-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-222] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-148] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-318] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-128] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [60-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [93-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [130-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 149, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [149-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-146] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [230-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-270] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [60-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [112-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-185] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-151] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [177-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-312] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-329] for track '33' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.