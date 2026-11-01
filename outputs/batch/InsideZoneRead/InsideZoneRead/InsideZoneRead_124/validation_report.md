# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_124`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [142–157], lower_priority='Action_ZoneBlock' annotated_start=146, effective_Action_ZoneBlock_start=158.
> - Action 'Action_BlockSecondLevel' range [159-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-274] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-233] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-253] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-282] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-253] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-297] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-327] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [186-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [285-292] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-263] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-292] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-219] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-262] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-285] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-313] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-333] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-174] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-213] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-189] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-243] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-273] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-257] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-352] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-244] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-339] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-278] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-297] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-303] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [323-327] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-334] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-315] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-343] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-334] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-322] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-339] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-336] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.