# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_2`
- **Input XML**: `output_showcase_final/Sack/Sack_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 27 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-165] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [174-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '19' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.