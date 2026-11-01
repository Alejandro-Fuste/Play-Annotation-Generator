# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_31`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '12' has invalid range: start=117, end=111. Clamping end to start.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [76–88], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=89.
> - Action 'Action_None' range [76-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-126] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [105-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-228] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [91-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-224] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-198] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-226] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-172] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-182] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-216] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '33' has 2 frames without a visible bounding box.
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