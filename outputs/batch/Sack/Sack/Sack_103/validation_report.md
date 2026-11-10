# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_103`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_103/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 45 |
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
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [175-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [187-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [191-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [206-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-184] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-210] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.