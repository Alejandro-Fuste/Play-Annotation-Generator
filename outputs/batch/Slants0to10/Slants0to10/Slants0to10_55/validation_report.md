# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_55`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 144 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [1–14], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=15.
> - Action 'Action_None' range [1-134] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-203] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-241] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-299] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [1-132] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-216] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-235] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-268] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-188] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-226] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-219] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-279] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [79-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-44] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-66] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-77] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-96] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-154] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-187] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-239] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-276] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-284] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-98] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-118] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-123] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-288] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-181] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-213] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-244] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-294] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-256] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-266] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-292] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-299] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-282] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '39' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.