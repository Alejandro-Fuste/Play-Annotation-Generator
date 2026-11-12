# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `SplitZone_292`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_292/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 26 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BlockSecondLevel' at frame 138 targets track ID '160', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '14' (DT) duration 175 frames exceeds threshold 90 frames [start=138, end=312].
> - Validation warning: Action 'Action_BlockSecondLevel' for track '16' (C) duration 150 frames exceeds threshold 90 frames [start=138, end=287].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [105–120], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=121.
> - Action 'Action_None' range [105-235] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-314] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-318] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-232] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [149-179] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-309] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [129-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-328] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [105-307] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [138-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [206-267] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [269-312] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-263] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-275] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-293] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [105-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [128-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [138-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [165-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [176-287] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-276] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-276] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-272] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-125] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-166] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.