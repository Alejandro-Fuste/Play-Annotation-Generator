# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_85`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
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
> - Action 'Action_None' range [61-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-225] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-133] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [60-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-184] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-196] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-136] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-159] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-158] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.