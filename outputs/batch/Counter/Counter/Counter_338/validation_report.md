# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_338`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_338/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [137–150], lower_priority='Action_DownBlock' annotated_start=140, effective_Action_DownBlock_start=151.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [137–150], lower_priority='Action_PlaySideFakeStep' annotated_start=145, effective_Action_PlaySideFakeStep_start=151.
> - Validation warning: Action 'Action_DownBlock' for track '12' (LT) duration 100 frames exceeds threshold 90 frames [start=140, end=239].
> - Validation warning: Action 'Action_DownBlock' for track '15' (LG) duration 100 frames exceeds threshold 90 frames [start=140, end=239].
> - Action 'Action_Handoff' range [166-185] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [140-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [164-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [177-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [199-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [211-227] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [229-231] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-282] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-317] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-289] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [305-323] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [325-353] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-389] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [151-262] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '7' starts at frame 186, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [186-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-195] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [228-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-294] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [140-199] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [140-165] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [193-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-216] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-243] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-263] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [140-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-386] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-174] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-181] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-221] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-389] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-382] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-254] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-306] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-389] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-389] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-328] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-389] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-375] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-384] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-380] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-380] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-381] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-389] for track '40' has 1 frames without a visible bounding box.
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