# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_18`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 38: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Deduplicated duplicate event 'Action_ComboBlock' at frame 189 for track '15'.
> - Action 'Action_PreSnap' range [0-273] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-290] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-296] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-317] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-304] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-281] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-290] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [213-257] for track '3' has 6 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [274-280] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [286-290] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [299-300] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-217] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [207-233] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-328] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-300] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-328] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [189-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-314] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-328] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-181] for track '14' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-224] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [189-207] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [217-230] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-254] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-311] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-318] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-327] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-193] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-208] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-223] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-250] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-267] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-311] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-321] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-280] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-310] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-327] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-322] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.