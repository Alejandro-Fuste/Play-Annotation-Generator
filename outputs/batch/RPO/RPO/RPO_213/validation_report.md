# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_213`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_213/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [59-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-209] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-126] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-198] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [74-123] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [127-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [166-204] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [214-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-116] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [59-131] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-226] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-234] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '20' starts at frame 60, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [60-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-171] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-158] for track '23' has 1 frames without a visible bounding box.
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