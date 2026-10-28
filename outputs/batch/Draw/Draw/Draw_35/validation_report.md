# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_35`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 155 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [31–47], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=48.
> - Action 'Action_None' range [31-60] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-254] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-279] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-286] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-66] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-93] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [101-112] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [31-63] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-82] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-257] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-63] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-101] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-48] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-289] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-265] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-294] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [52-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '17' starts at frame 76, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [76-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-61] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [31-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-59] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [31-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-54] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-290] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-161] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-178] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-265] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-288] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-294] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-182] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-264] for track '26' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-294] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-151] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-174] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-268] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-248] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-264] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-222] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-299] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-235] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-288] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-228] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-252] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-266] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-280] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-299] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-288] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '43' has 1 frames without a visible bounding box.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.