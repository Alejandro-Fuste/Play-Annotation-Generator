# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_99`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [31-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-154] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '10' starts at frame 32, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [32-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-39] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-62] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-69] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-80] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 32, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [32-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-180] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-95] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.