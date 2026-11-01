# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_90`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_90/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 27 |
| Ball Tracks | 2 |
| CSV events parsed | 21 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [138–155], lower_priority='Action_ZoneBlock' annotated_start=141, effective_Action_ZoneBlock_start=156.
> - Action 'Action_PreSnap' range [0-125] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-217] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-208] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-203] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-237] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-206] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [210-303] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-320] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-182] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [187-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-203] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-272] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-244] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-254] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-313] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.