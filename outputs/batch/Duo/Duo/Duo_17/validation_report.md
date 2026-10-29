# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_17`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 35: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Segment 'Action_ComboBlock' for track '17' has invalid range: start=201, end=186. Clamping end to start.
> - Action 'Action_PreSnap' range [0-243] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-262] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-292] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-273] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-249] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [263-264] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-304] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-320] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-283] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-319] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-322] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-248] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-260] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-191] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-206] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-328] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-285] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-311] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-242] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-248] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-259] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-273] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-305] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-136] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-292] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-128] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-287] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-260] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-271] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-298] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-310] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-328] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-297] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-310] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-315] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-301] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-328] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-323] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-303] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.