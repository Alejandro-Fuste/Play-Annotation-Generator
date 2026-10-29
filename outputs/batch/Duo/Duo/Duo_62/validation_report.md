# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_62`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '15' has invalid range: start=28, end=19. Clamping end to start.
> - Action 'Action_PreSnap' range [0-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-149] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-53] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '10' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [32-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-149] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '16' starts at frame 28, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [28-28] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [48-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [52-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [63-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-121] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-95] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [77-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [85-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-149] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.