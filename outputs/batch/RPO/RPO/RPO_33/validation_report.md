# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_33`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
> - Action 'Action_None' range [49-115] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-127] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-146] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [77-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [95-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-52] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-160] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-133] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-329] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-187] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '26' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.