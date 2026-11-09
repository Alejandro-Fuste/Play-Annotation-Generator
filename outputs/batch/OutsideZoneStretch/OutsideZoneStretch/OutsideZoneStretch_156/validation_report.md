# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_156`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_156/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-164] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-161] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-124] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-145] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-172] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [55-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 73, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [73-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-85] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-163] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.