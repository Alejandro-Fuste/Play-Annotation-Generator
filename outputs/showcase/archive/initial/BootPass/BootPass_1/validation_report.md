# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_1`
- **Input XML**: `output_showcase/BootPass/BootPass_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 200 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 4: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 4: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [71–86], lower_priority='Action_RunBlock' annotated_start=77, effective_Action_RunBlock_start=87.
> - Action 'Action_None' range [71-359] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-286] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-316] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-332] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-285] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-311] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-170] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-197] for track '6' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [200-359] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-183] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [71-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-173] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-282] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-311] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-336] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [77-187] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-197] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-251] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-298] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-333] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [77-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [88-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [94-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [119-164] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [171-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [176-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [194-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [213-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [222-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [231-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [235-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [239-240] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-179] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [71-83] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [87-170] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [173-191] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [196-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [238-257] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [260-359] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-112] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-27] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [78-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-122] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-162] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-200] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-198] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-257] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-291] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-178] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-270] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-312] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-332] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-199] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-282] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-227] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-244] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-296] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [303-315] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [338-359] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-227] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-246] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-252] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-281] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-307] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-319] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-249] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-257] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-336] for track '32' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [340-359] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-254] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-274] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-359] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-284] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-348] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-260] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-297] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-317] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [326-330] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-359] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-278] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-319] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [338-359] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-310] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-347] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '40' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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