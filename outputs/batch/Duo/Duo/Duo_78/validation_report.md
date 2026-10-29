# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_78`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 42 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '12' has invalid range: start=152, end=125. Clamping end to start.
> - Deduplicated duplicate event 'Action_ComboBlock' at frame 152 for track '18'.
> - Segment 'Action_ComboBlock' for track '18' has invalid range: start=152, end=116. Clamping end to start.
> - Action 'Action_PreSnap' range [0-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-179] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-166] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [168-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [177-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-146] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-24] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-179] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.