# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_71`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 178 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 144: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 112 frames exceeds threshold 90 frames [start=101, end=212].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 112 frames exceeds threshold 90 frames [start=101, end=212].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 112 frames exceeds threshold 90 frames [start=101, end=212].
> - Segment 'Action_BallSnap' for track '14' has invalid range: start=97, end=50. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '14' has invalid range: start=101, end=50. Clamping end to start.
> - Action 'Action_PreSnap' range [0-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-222] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-276] for track '0' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [288-313] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-181] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_Toss' range [116-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-257] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-291] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-158] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-242] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-173] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-236] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-56] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-199] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-205] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [207-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-263] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-160] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-300] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-312] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-38] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [70-111] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [113-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [120-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-141] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-176] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [179-212] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-277] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-236] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-215] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-275] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-294] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-225] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-281] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [291-301] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-327] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-276] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-291] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [204-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-262] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-275] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-291] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-296] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-311] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-321] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-243] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-263] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-327] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [243-256] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-274] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-287] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-329] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-328] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-329] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-306] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-302] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-327] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '50' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.