# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_118`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_118/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
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
> - Segment 'Action_ComboBlock' for track '11' has invalid range: start=158, end=123. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '15' has invalid range: start=158, end=149. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '17' has invalid range: start=158, end=90. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '17' has invalid range: start=190, end=90. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '19' has invalid range: start=158, end=149. Clamping end to start.
> - Action 'Action_PreSnap' range [0-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-149] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-105] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-108] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-106] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-111] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-149] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-149] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.