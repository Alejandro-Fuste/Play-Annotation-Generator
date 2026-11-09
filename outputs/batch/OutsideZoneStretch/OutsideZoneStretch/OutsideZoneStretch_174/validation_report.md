# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_174`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_174/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-80] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-204] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-64] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-166] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '25' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.