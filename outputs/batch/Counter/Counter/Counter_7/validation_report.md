# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_7`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 131 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 16: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 16: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_BallCarry' range [250-276] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [278-389] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [217-256] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [259-294] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-311] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-389] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-273] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-270] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [217-226] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [229-231] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [234-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [300-303] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-389] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-251] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-265] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [240-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-388] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-12] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-363] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-389] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-54] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [219-243] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-12] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '17' starts at frame 217, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [217-217] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-240] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [245-252] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [260-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-275] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [279-303] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-322] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-348] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-357] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-224] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [217-226] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-252] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [255-274] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [279-290] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-369] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-389] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-205] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-148] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-297] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-289] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-302] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-310] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-354] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [356-362] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-325] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-345] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-358] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [361-367] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-376] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-382] for track '29' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.