# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_66`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 134: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [164–178], lower_priority='Action_ZoneBlock' annotated_start=167, effective_Action_ZoneBlock_start=179.
> - Action 'Action_PreSnap' range [0-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-307] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-227] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-309] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-336] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [341-342] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-237] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-318] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-351] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-277] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-243] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-234] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [237-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-302] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-333] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-351] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-348] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-326] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-333] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-279] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '23' starts at frame 164, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [164-172] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-294] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-265] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-300] for track '29' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.