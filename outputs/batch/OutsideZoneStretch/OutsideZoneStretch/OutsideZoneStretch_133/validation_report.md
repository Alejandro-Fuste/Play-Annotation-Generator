# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_133`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_133/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [168-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-202] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-299] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '26' has 1 frames without a visible bounding box.
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