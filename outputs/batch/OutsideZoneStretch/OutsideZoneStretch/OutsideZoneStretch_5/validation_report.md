# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_5`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 38 |
| Ball Tracks | 1 |
| CSV events parsed | 13 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 12: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_Handoff' for track '13' has invalid range: start=109, end=63. Clamping end to start.
> - Action 'Action_PreSnap' range [0-196] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-258] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-277] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-308] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-312] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-219] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-190] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-255] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-304] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-312] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-326] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-63] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-265] for track '12' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-305] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-187] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-97] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-117] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-4] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [56-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-257] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-291] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-323] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-196] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-215] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-245] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-267] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-257] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-256] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-243] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-309] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-274] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-307] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-329] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-317] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-318] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '38' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.