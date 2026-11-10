# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_215`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_215/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 400: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [37-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-237] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-233] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-217] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [45-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-80] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '20' starts at frame 38, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [38-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-195] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '30' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.