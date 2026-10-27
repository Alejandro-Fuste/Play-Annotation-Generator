# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_125`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [143–156], lower_priority='Action_DownBlock' annotated_start=148, effective_Action_DownBlock_start=157.
> - Action 'Action_None' range [143-224] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-283] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-248] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-284] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-295] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-287] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-301] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-198] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-289] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [144-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [230-287] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-290] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [240-246] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [148-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-183] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-278] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-304] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-273] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-316] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-249] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-254] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-282] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-298] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-271] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-298] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [301-316] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-295] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-295] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-329] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '37' has 1 frames without a visible bounding box.
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