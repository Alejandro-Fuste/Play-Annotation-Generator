# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_59`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 120: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '15' has invalid range: start=170, end=137. Clamping end to start.
> - Action 'Action_PreSnap' range [0-194] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-215] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-263] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-326] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-320] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-273] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-222] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-216] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-173] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-243] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-297] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-255] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-266] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-307] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-329] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-311] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-320] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-280] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-263] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-273] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-303] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-308] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-302] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-326] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-322] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-272] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-321] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-297] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '31' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.