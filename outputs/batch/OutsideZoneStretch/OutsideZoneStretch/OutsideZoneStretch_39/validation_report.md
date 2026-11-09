# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_39`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 80: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-212] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-332] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-315] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-243] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-175] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-359] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-191] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-231] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-178] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-308] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-305] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-247] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-66] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_Keep' range [124-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [188-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-210] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-201] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-289] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-245] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-332] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-254] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-312] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-228] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-271] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-295] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-288] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-251] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-313] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-333] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-339] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-356] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-350] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-303] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-359] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-334] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-312] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-327] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-331] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-341] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-348] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-358] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-345] for track '44' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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