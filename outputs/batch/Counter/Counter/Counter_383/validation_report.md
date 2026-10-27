# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_383`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_383/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 768: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [211–226], lower_priority='Action_DownBlock' annotated_start=214, effective_Action_DownBlock_start=227.
> - Action 'Action_None' range [211-243] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-322] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-355] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-370] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-332] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [214-272] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-340] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-428] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-437] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-449] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-297] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-293] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-342] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-242] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-266] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-271] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-374] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [211-314] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [240-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-332] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [227-231] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [241-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-242] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-241] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-281] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-341] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [360-367] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [214-241] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [256-277] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [282-285] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-356] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-284] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-46] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [214-255] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [263-264] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [266-274] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-429] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-230] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [224-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [242-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-317] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-449] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-321] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-346] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-361] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-274] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-309] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-316] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-305] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-344] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [350-393] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-351] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-426] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-325] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-335] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-377] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-449] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-345] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-399] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-382] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-419] for track '35' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [422-449] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-381] for track '36' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.