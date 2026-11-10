# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_34`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 60: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '20' has invalid range: start=28, end=24. Clamping end to start.
> - Action 'Action_None' range [27-87] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [91-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-37] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-98] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-210] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-72] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-77] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-81] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-208] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-197] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '32' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.