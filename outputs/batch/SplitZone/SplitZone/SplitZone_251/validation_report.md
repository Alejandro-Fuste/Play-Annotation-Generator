# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_251`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_251/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 136 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 504: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '18' has invalid range: start=129, end=114. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [92–100], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=101.
> - Action 'Action_None' range [92-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-121] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-281] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-293] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-161] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-193] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-231] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-127] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-121] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-162] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [92-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-262] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [264-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-287] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-297] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-198] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-272] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-299] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-243] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-273] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [275-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [132-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-293] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-152] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-121] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-114] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-121] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-273] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-293] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-223] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-289] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-293] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-273] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-293] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-273] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-281] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-299] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-286] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '34' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.