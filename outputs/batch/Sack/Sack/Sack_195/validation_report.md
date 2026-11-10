# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_195`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_195/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 17 |
| Player Tracks | 17 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 24 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [162-180] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [177-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-162] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-175] for track '16' has 2 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.