# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_11`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [29-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-168] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-83] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-68] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-166] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-102] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 104, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [104-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-165] for track '27' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.