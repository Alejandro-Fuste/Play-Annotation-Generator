# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_143`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_143/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-271] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-277] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-278] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-225] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-315] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-309] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-321] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-228] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-35] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-276] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-205] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-302] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.