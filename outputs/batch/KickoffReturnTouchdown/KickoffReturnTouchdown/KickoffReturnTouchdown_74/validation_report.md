# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_74`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 150: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Action 'Action_None' range [6-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-203] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-231] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-253] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-402] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-446] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-297] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-430] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-404] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-537] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [6-539] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [6-508] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-470] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-164] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-177] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-274] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-539] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-165] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-234] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-274] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-375] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-522] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-213] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-237] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-231] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-440] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-240] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-253] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-291] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-408] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-445] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-299] for track '26' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [247-539] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-401] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-421] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-298] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-389] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-309] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-421] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-398] for track '33' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [404-417] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-442] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-399] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-412] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-428] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-442] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-462] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-472] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-480] for track '37' has 2 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.