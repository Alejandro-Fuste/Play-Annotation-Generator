# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_237`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_237/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
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
> - Action 'Action_None' range [30-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-152] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-102] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [34-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-115] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-51] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-88] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 31, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [31-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-51] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-124] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.