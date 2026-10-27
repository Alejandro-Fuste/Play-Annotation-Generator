# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_211`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_211/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 140 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 423: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 424: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_None' range [73-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-389] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-125] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-164] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-184] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-221] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-257] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-361] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-388] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [76-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [127-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-185] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-202] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-346] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-362] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-381] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-389] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-243] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-165] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [106-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-295] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-308] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-209] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-220] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-250] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-326] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-357] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-365] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-227] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-250] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-351] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-359] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-363] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-379] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-379] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-385] for track '45' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.